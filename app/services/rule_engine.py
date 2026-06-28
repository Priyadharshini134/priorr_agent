def evaluate_policy(patient_data, policy_rules):

    observations = patient_data["observations"]

    results = []

    has_fail = False
    has_missing = False

    for rule in policy_rules:

        rule_name = rule["rule_name"]
        operator = rule["operator"]
        expected = rule["expected_value"]

        actual = observations.get(rule_name)

        # ------------------------
        # Missing Observation
        # ------------------------

        if actual is None:

            results.append({

                "rule": rule_name,

                "expected": expected,

                "actual": None,

                "status": "MISSING"

            })

            has_missing = True
            continue

        # ------------------------
        # Rule Evaluation
        # ------------------------

        try:

            if operator == ">":

                status = (
                    "PASS"
                    if float(actual) > float(expected)
                    else "FAIL"
                )

            elif operator == "<":

                status = (
                    "PASS"
                    if float(actual) < float(expected)
                    else "FAIL"
                )

            elif operator == ">=":

                status = (
                    "PASS"
                    if float(actual) >= float(expected)
                    else "FAIL"
                )

            elif operator == "<=":

                status = (
                    "PASS"
                    if float(actual) <= float(expected)
                    else "FAIL"
                )

            elif operator == "=":

                status = (
                    "PASS"
                    if str(actual).lower() == str(expected).lower()
                    else "FAIL"
                )

            else:

                status = "INVALID"

        except:

            status = "INVALID"

        if status == "FAIL":

            has_fail = True

        results.append({

            "rule": rule_name,

            "expected": expected,

            "actual": actual,

            "status": status

        })

    # ------------------------
    # Overall Status
    # ------------------------

    if has_missing:

        overall = "Pending"

    elif has_fail:

        overall = "Not Eligible"

    else:

        overall = "Eligible"

    return {

        "results": results,

        "overall_status": overall

    }