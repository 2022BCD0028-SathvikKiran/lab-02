import json
import argparse
import os

def find_file(candidates):
    for c in candidates:
        if os.path.exists(c):
            return c
    return None

def main():
    parser = argparse.ArgumentParser(description='Parse GitHub Actions runs JSON')
    parser.add_argument('--file', '-f', help='Path to actions_runs.json', default=None)
    args = parser.parse_args()

    candidates = []
    if args.file:
        candidates.append(args.file)
    candidates.extend(['actions_runs.json', os.path.join('lab2', 'actions_runs.json'), os.path.join('lab2', 'Script', 'actions_runs.json')])

    p = find_file(candidates)
    if not p:
        print('No actions_runs.json found in candidates:', candidates)
        return

    with open(p, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)

    runs = data.get('workflow_runs', [])
    if not runs:
        print('No runs found in', p)
        return

    # print a brief top-5 summary
    for i, r in enumerate(runs[:5], start=1):
        print(i, r.get('id'), r.get('name'), r.get('head_branch'), r.get('status'), r.get('conclusion'))

    latest = runs[0]
    print('\nLatest run id:', latest.get('id'))
    print('logs_url:', latest.get('logs_url'))
    print('html_url:', latest.get('html_url'))

    # write a small summary to output/actions_summary.json
    os.makedirs('output', exist_ok=True)
    summary = {
        'source_file': p,
        'latest_run': {
            'id': latest.get('id'),
            'name': latest.get('name'),
            'branch': latest.get('head_branch'),
            'status': latest.get('status'),
            'conclusion': latest.get('conclusion'),
            'html_url': latest.get('html_url'),
            'logs_url': latest.get('logs_url'),
            'created_at': latest.get('created_at')
        },
        'top_runs_count': min(5, len(runs))
    }

    out_path = os.path.join('output', 'actions_summary.json')
    with open(out_path, 'w', encoding='utf-8') as out_f:
        json.dump(summary, out_f, indent=2)

    print(f"Wrote summary to {out_path}")

if __name__ == '__main__':
    main()
