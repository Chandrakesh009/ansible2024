
#!/usr/bin/env python3
import json
import sys

def main():
    # Handle arguments (e.g., --list or --host <hostname>)
    if len(sys.argv) == 2 and sys.argv[1] == '--list':
        # Generate the inventory as a JSON object
        inventory = {
            "web": {
                "hosts": ["192.168.10.196"],
                "vars": {
                    "http_port": 80,
                    "max_clients": 200
                }
            },
            "db": {
                "hosts": ["192.168.10.198"],
                "vars": {
                    "db_port": 5432,
                    "db_user": "admin"
                }
            },
            "_meta": {
                "hostvars": {
                    "192.168.10.196": {
                        "ansible_user": "ansible"
                    },
                    "192.168.10.198": {
                        "ansible_user": "ansible"
                    }
                }
            }
        }
        print(json.dumps(inventory))
    elif len(sys.argv) == 3 and sys.argv[1] == '--host':
        # Return details about a single host
        host = sys.argv[2]
        hostvars = {
            "192.168.10.196": {
                "ansible_user": "ansible"
            },
            "192.168.10.198": {
                "ansible_user": "ansible"
            }
        }
        print(json.dumps(hostvars.get(host, {})))
    else:
        # Invalid or unsupported arguments
        print(json.dumps({}))
        sys.exit(1)

if __name__ == "__main__":
    main()

