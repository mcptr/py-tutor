# This is the file with empty functions which you needs update to
# implement yourself.
#
# Note:
# You can test your solutions by running "python3 test.py" or "make test".
#
# You can find servers.json file and inspect its contents.
# That json file contains random data representing server clusters.
#
# Assignment: Implement each function below as documented in its docstring.
#
# Additional assignments:
# - write a function that updates all server passwords
# - write a function that find out which server is the oldest
# - write a function that prints a "LOW LOAD [server_id]" for servers
#   which have load_avg[2] less than 0.32
# - write a function which sets an "needs_update: 1" key in all servers
#   whose "os" attribute's value does not contain "latest"
# - write a function lists server ids grouped in a dict using os as a key, e.g:
#   { "debian:latest": ["fe6b41310915", "94bfeae948ee", ...],
#     "alpine:latest": ["a92b0b3ff89b", "4ad01640d667", ..., "4a415bbb5f38", ],
#      ...
#   }
# - write a function that format each server prints its processes sorted
# - write a function that changes "example.com" to "example.net" in all admin_emails
#   (in clusters and servers)
# - write a function which validates that all admin_emails are valid emails



def count_clusters(clusters):
    """Returns total number of clusters"""
    pass


def get_cluster_names(clusters):
    """Returns a list of cluster names in ascending alphabetical order"""
    pass


def count_servers(cluster):
    """Returns number of servers in a given cluster"""
    pass


def map_servers_by_operating_system(clusters, os_name):
    """Returns a dict: server id => cluster id for servers
    running the given operating system (os_name)"""
    pass


def get_server_names_by_total_cpus(clusters):
    """Returns a list of server names sorted by the total number
    of cpus in ascending order"""
    # 6a850a2942af 1
    # 5d75d91d6c71 2
    # ...
    # 4ad01640d667 16
    # b00ba9e9359c 16
    pass


def filter_at_least_4gb_mem(clusters):
    """Returns a list of server ids of servers having at least 4096 gb memory"""
    pass


def filter_uptime_gt_30days(clusters):
    """Returns a list of id:ip4 strings of servers not restarted in 30 days
    (use uptime_seconds)"""
    # "a92b0b3ff89b:172.16.108.206",
    # "4ad01640d667:172.16.242.32",
    # ...
    #"798048331494:172.16.59.118",
    # "000f0bd81683:172.16.144.19",
    pass


def filter_nginx_locations(clusters):
    """Returns a list of locations of servers running
    at least 3 nginx processes"""
    # eu-nl
    # us-west-2
    # jp-tokyo
    pass


def calculate_total_load_per_cluster(clusters):
    """Calculates total load average per cluster using formula:
    1. sum load_avg[0] of all servers in a cluster
    2. divide the total sum by the number of servers in a cluster

    Round the results to 2 significant numbers.
    The output should be a dict:

    {
        "cluster-7d0ef71bb739": (7.24, 1.21),
        "cluster-a8b1638a519d": (4.54, 1.14),
        "cluster-2dfe2c77e9c6": (3.89, 0.78),
    }
    """
    pass
