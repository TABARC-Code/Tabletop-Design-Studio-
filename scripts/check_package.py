"""Offline package integrity checks. No files are executed or changed."""
import csv
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


def local_target(root, source, target):
    parts = urlsplit(target)
    if parts.scheme and parts.scheme not in {'https', 'http', 'mailto'}:
        return f'{source.relative_to(root)}: unsupported link scheme: {parts.scheme}'
    if parts.scheme or parts.netloc or not parts.path:
        return None
    path = (source.parent / unquote(parts.path)).resolve()
    if not path.is_relative_to(root.resolve()):
        return f'{source.relative_to(root)}: path escapes package: {target}'
    if not path.exists():
        return f'{source.relative_to(root)}: missing path: {target}'
    return None


def check(root):
    root = root.resolve()
    errors = []
    markdown = sorted(root.rglob('*.md'))
    for source in markdown:
        content = source.read_text(encoding='utf-8')
        targets = re.findall(r'\]\(([^\s)]+)\)', content)
        targets += re.findall(r'`(\.\./[^`]+)`', content)
        for target in targets:
            error = local_target(root, source, target)
            if error:
                errors.append(error)
    skill = (root / 'SKILL.md').read_text(encoding='utf-8')
    for target in re.findall(r'`((?:references|templates|contracts|data)/[^`]+)`', skill):
        error = local_target(root, root / 'SKILL.md', target)
        if error:
            errors.append(error)
    if not skill.startswith('---\n') or not re.search(r'^name: [a-z0-9-]+$', skill, re.M):
        errors.append('SKILL.md: invalid name/frontmatter')
    if not re.search(r'^description: .+', skill, re.M):
        errors.append('SKILL.md: missing description')
    schema = json.loads((root / 'contracts/design_brief_v1.schema.json').read_text())
    metrics = schema['properties']['success_metrics']
    if (metrics.get('minItems'), metrics.get('maxItems')) != (2, 4):
        errors.append('design brief: success metrics must contain two to four items')
    path = root / 'data/tabletop_playtester_profiles_FULL_1_380_claude_skill.csv'
    with path.open(encoding='utf-8', newline='') as stream:
        reader = csv.DictReader(stream)
        columns = ['#', 'Name', 'Age', 'Gender', 'Sexuality', 'SES', 'Experience', 'Primary Types', 'Play Style', 'Key Testing Focus']
        if reader.fieldnames != columns:
            errors.append('persona CSV: unexpected columns')
        rows = list(reader)
    ids = [row.get('#') for row in rows]
    if len(rows) != 380 or set(ids) != {str(i) for i in range(1, 381)}:
        errors.append('persona CSV: expected unique IDs 1 to 380')
    if any(None in row or any(not value for value in row.values()) for row in rows):
        errors.append('persona CSV: missing values or inconsistent row width')
    example = (root / 'examples/example_playtest_report.md').read_text()
    example_id = re.search(r'^tester_id: (\d+)$', example, re.M)
    example_name = re.search(r'^tester_name: (.+)$', example, re.M)
    if example_id and example_name:
        matches = [row for row in rows if row.get('#') == example_id[1]]
        if len(matches) != 1 or matches[0].get('Name') != example_name[1]:
            errors.append('example report: tester ID/name mismatch')
    for source in (root / 'references/rules').glob('*.md'):
        if re.search(r'/mnt/skills/|/areas/|(?:rules-clarity-drafter|rules-register-orchestrator)/', source.read_text()):
            errors.append(f'{source.relative_to(root)}: obsolete external filesystem contract')
    return errors


if __name__ == '__main__':
    problems = check(Path(__file__).resolve().parents[1])
    for problem in problems:
        print(problem)
    print(f'Package integrity: {len(problems)} problem(s)')
    sys.exit(bool(problems))
