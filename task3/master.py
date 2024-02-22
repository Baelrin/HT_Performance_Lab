import json
import sys
import os


def fill_report(tests, values):
    """
    Fills out the report with values from values using the structure defined in tests.
    :param tests: Dictionary defining the structure of the report.
    :param values: Dictionary with test results.
    :return: Dictionary filled with values.
    """
    for key, value in tests.items():
        if isinstance(value, dict):
            fill_report(value, values)
        elif key == "value":
            tests[key] = values.get(value, "Not found")
    return tests


def main(values_path, tests_path, report_path):
    """
    Main function of the program.
    :param values_path: Path to the file with test results.
    :param tests_path: Path to the file with the report structure.
    :param report_path: Path to the file to save the report.
    """
    # Checking that all paths point to valid files
    if not (os.path.exists(values_path) and os.path.exists(tests_path)):
        print(f"File not found: {values_path}, {tests_path}")
        return

    try:
        with open(values_path, 'r') as f:
            values = json.load(f)
        with open(tests_path, 'r') as f:
            tests = json.load(f)
        report = fill_report(tests, values)
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=4)
            print(f"Report saved to {report_path}")
    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")
    except json.JSONDecodeError:
        print("Error reading JSON file. Ensure the files contain valid JSON.")
    except OSError:
        print("Error writing to file. Ensure you have write permissions to the specified file.")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python master.py <values.json> <tests.json> <report.json>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3])
