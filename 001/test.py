import solutions


########################################################################
# DO NOT MODIFY THE CODE BELOW
########################################################################
if __name__ == "__main__":
    import devops

    clusters = devops.load_clusters("servers.json")
    # devops.display(clusters)

    totals = {
        "cluster-2dfe2c77e9c6": 5,
        "cluster-7d0ef71bb739": 6,
        "cluster-a8b1638a519d": 4,
    }

    mapping = {
        "a92b0b3ff89b": "7d0ef71bb739",
        "4ad01640d667": "7d0ef71bb739",
        "886a2468c593": "7d0ef71bb739",
        "5d75d91d6c71": "a8b1638a519d",
        "4a415bbb5f38": "2dfe2c77e9c6"
    }

    by_cpu = [
        "6a850a2942af",
        "5d75d91d6c71",
        "94bfeae948ee",
        "fe6b41310915",
        "886a2468c593",
        "968b99521695",
        "3c51259125b4",
        "000f0bd81683",
        "a92b0b3ff89b",
        "bc589d9c7479 ",
        "f774f2ac67e7 ",
        "798048331494 ",
        "4a415bbb5f38 ",
        "4ad01640d667 ",
        "b00ba9e9359c ",
    ]

    uptime_gt_30_days = [
        "a92b0b3ff89b:172.16.108.206",
        "4ad01640d667:172.16.242.32",
        "fe6b41310915:172.16.117.66",
        "968b99521695:172.16.113.201",
        "bc589d9c7479:172.16.217.21",
        "3c51259125b4:172.16.96.66",
        "94bfeae948ee:172.16.127.70",
        "f774f2ac67e7:172.16.4.91",
        "6a850a2942af:172.16.253.202",
        "b00ba9e9359c:172.16.150.25",
        "798048331494:172.16.59.118",
        "000f0bd81683:172.16.144.19",
    ]

    nginx_locations = [
        "eu-nl",
        "us-west-2",
        "jp-tokyo",
    ]

    total_cluster_avg = {
        "cluster-7d0ef71bb739": (7.24, 1.21),
        "cluster-a8b1638a519d": (4.54, 1.14),
        "cluster-2dfe2c77e9c6": (3.89, 0.78),
    }

    assert solutions.count_clusters(clusters) == 3, "count_clusters"

    assert get_cluster_names(clusters) == [
        'cluster-46ae2a73348f',
        'cluster-71f326eef11b',
        'cluster-b748faa818b3'
    ], "get_cluster_names"

    for k, n in totals.items():
        assert solutions.count_servers(k) == n, "count_servers: %s" % k

    assert solutions.map_servers_by_operating_system(
        clusters, "alpine:latest") == mapping

    assert solutions.filter_at_least_4gb_mem(clusters) == [
        "a92b0b3ff89b",
        "886a2468c593",
        "f774f2ac67e7",
        "4a415bbb5f38"
    ]

    assert solutions.filter_uptime_gt_30days(clusters) == uptime_gt_30_days

    assert solutions.filter_nginx_locations(clusters) == nginx_locations

    totals = solutions.calculate_total_load_per_cluster(clusters)
    for c in total_cluster_avg:
        assert totals[c][0] == total_cluster_avg[c][0]
        assert totals[c][1] == total_cluster_avg[c][1]
