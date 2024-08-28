#import your own dataset attributes and generate 
from faker import Faker
import os

# Initialize Faker and setup
fake = Faker()

# Directory to save text files
output_dir = 'IT_Policies'
os.makedirs(output_dir, exist_ok=True)

def generate_policy_paragraph(policy_id):
    policy_name = fake.bs().title()
    department = random.choice(['IT', 'HR', 'IT Security', 'All', 'Facilities'])
    effective_date = fake.date_this_decade()
    review_date = fake.date_this_decade()
    status = random.choice(['Active', 'Inactive'])
    compliance_required = random.choice([True, False])
    last_updated_by = fake.name()
    comments = fake.sentence()

    policy_description = (
        f"The {policy_name} policy requires all employees to follow specific guidelines for maintaining "
        "secure and efficient IT operations. This policy outlines the procedures and requirements for "
        "ensuring the proper use and management of company resources. Employees must adhere to the prescribed "
        "standards and practices to remain compliant with this policy. The policy will be reviewed periodically "
        "to ensure its effectiveness and relevance. Failure to comply with the policy may result in disciplinary "
        "action. Please refer to the policy documentation for detailed guidelines and requirements."
    )

    content = (
        f"**Policy ID:** {policy_id}\n"
        f"**Policy Name:** {policy_name}\n"
        f"**Policy Description:** {policy_description}\n"
        f"**Department:** {department}\n"
        f"**Effective Date:** {effective_date}\n"
        f"**Review Date:** {review_date}\n"
        f"**Status:** {status}\n"
        f"**Compliance Required:** {compliance_required}\n"
        f"**Last Updated By:** {last_updated_by}\n"
        f"**Comments:** {comments}\n"
    )

    return content

def save_policy_files(n=10000):
    for i in range(1, n+1):
        policy_text = generate_policy_paragraph(i)
        with open(f'{output_dir}/Policy_{i}.txt', 'w') as file:
            file.write(policy_text)

# Generate the policies
save_policy_files()
