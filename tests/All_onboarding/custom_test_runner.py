import subprocess

# Define the test classes to run sequentially
test_classes = [
    "test_onboarding_doc.py::TestDoctoronboarding",
    "test_onboardinng_pat.py::TestPatientOnboarding",
]

# Run the test classes sequentially in separate workers
for test_class in test_classes:
    subprocess.call(['pytest', '-n1', test_class])
