import pto

print(f"Test 001 - Register site (good): {pto.register_site('Test')}")
print(f"Test 002 - Both dates (good): {pto.add_pto('Test', 'Bill', 'Germany trip', '2022-08-01', '2022-08-20')}")
print(f"Test 003 - Just from date (good): {pto.add_pto('Test', 'Sarah', 'Texas', '2022-08-01')}")
print(f"Test 004 - Invalid from date (error): {pto.add_pto('Test', 'Fred', 'Doctor', 'cow', '2022-08-20')}")
print(f"Test 005 - Invalid to date (error): {pto.add_pto('Test', 'Mary', 'Germany trip', '2022-08-01', 'cow')}")

print(f"Test 006 - View PTO: {pto.view_pto()}")
