import requests
import sys
import json
from datetime import datetime
import os

now = datetime.now()

base_url = 'https://sonarcloud.io/api/measures/component_tree?component=fga-eps-mds_2021-2-PUMA-'

metrics = ['files', 'functions', 'complexity', 'comment_lines_density', 'duplicated_lines_density',
           'coverage', 'ncloc', 'tests', 'test_errors', 'test_failures', 'test_execution_time', 'security_rating']

file_name = 'fga-eps-mds-2021-2-PUMA'


def consumer(repository, version):
    metrics_str = ",".join(metrics)
    print(metrics_str)
    res = requests.get(base_url+repository +
                       '&metricKeys='+metrics_str+'&ps=500')
    m = res.json()
    f = open(
        f'./analytics-raw-data/{file_name}-{repository}-{now.strftime("%m-%d-%Y-%H:%M:%S")}-v{version}.json', 'w')
    f.write(json.dumps(m, indent=4))
    f.close()


if __name__ == '__main__':
    # Verification Path
    folder = 'analytics-raw-data'
    create_folder = os.path.exists(folder)
    if not create_folder:
        os.makedirs(folder)

    repository = sys.argv[1]
    version = sys.argv[2]
    consumer(repository, version)