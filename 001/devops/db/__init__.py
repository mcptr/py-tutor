import json
import os
import uuid
import random
import logging
import string
from datetime import datetime, timedelta


log = logging.getLogger(__name__)


LOCATIONS = [
    "us-west-1", "us-west-2",
    "us-east", "us-central",
    "eu-nl", "eu-se", "eu-pl",
    "singapore", "jp-tokyo",
]

def load_servers(path):
    with open(path, "r") as db_file:
        return json.load(db_file)


def load_random_db():
    return generate_random_db()


def _gen_random_ip4():
    return "172.16.%d.%d" % (random.randint(2, 254), random.randint(2, 254))


def _gen_random_passwd(n=8):
    chars = string.ascii_lowercase + string.digits
    return "".join([random.choice(chars) for _ in range(n)])


def _gen_random_processlist(n=4):
    services = ["openvpn", "vsftpd", "nginx", "uwsgi"]
    return [random.choice(services) for _ in range(n)]


def gen_random_servers():
    domain = random.choice([
        "example.com", "virtual.tld", "localdomain"
    ])
    clusters = {}
    for i in range(3):
        cluster_uuid = str(uuid.uuid4()).split("-")[-1]
        cluster_id = "cluster-%s" % cluster_uuid
        log.debug("Generating cluster cluster %s", cluster_id)
        ctime = datetime.now() - timedelta(days=random.randint(30, 180))
        clusters[cluster_id] = dict(
            id=cluster_uuid,
            servers=[],
            ctime=ctime.isoformat(),
            admin_email="cluster-admin@%s.srv-%d.%s" % (cluster_id, i, domain),
        )

    for cluster_id in sorted(clusters):
        for i in range(random.randint(3, 7)):
            srv_uuid = str(uuid.uuid4()).split("-")[-1]
            srv_id = "srv-%s" % srv_uuid
            log.debug(
                "Adding server %s list to cluster %s",
                srv_id, cluster_id)

            clusters[cluster_id]["servers"].append(
                dict(
                    id=srv_uuid,
                    ip4=_gen_random_ip4(),
                    password=_gen_random_passwd(random.randint(8, 16)),
                    admin_email="root@%s.srv-%d.%s" % (srv_id, i, domain),
                    location=random.choice(LOCATIONS),
                    cpus=random.randint(1, 16),
                    memory=random.choice([256, 512, 1024, 2048, 4096, 8192]),
                    os=random.choice([
                        "debian:latest", "centos:7",
                        "ubuntu:18.04", "alpine:latest"]),
                    stats=dict(
                        load_avg=(
                            round(random.random() * 10 % 2, 2),
                            round(random.random() * 10 % 4, 2),
                            round(random.random(), 2),
                        ),
                        uptime_seconds=random.randint(600, 3600 * 24 * 180),
                        processes=_gen_random_processlist(random.randint(2, 8)),
                    ),
                )
            )
    return clusters
