if __name__ == '__main__':
    inputt = ["neighbor", "description", "network", "router bgp", "router rip", "router ospf", "hostname"]
    pref = "ka"
    id = 0
    for i in inputt:
        print(
            "\t\"" + pref + str(id) + "\":{\n\t\t\"prefix\": [\"" + i + "\"],\n\t\t\"body\": [\"" + i + "\"],\n\t},")
        id += 1
