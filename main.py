import boto3

def main():
    session = boto3.Session(
        profile_name = 'default',
        region_name = 'us-east-1'
    )

    sns_connection = session.client('sns')
    response = sns_connection.publish(
        PhoneNumber = '+5585911112222', # Use E.164 format. DDD without the 0(zero).
        Message = 'devops: Test send SMS.'
    )

    print(response)

if __name__ == '__main__':
    main()
