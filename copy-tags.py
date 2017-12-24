#!/usr/bin/env python
'''
Copy EC2 tags from a source instance to destination instance.

..moduleauthor:: Mike Pietruszka <mike@mpietruszka.com>
'''

import boto3
import sys
import argparse


def copy_tags(region, src_instance_id, dst_instance_id):
    try:
        session = boto3.session.Session(region_name=region)
    except:
        raise Exception("ERROR: error")
    else:    
        ec2_client = session.client('ec2')
        ec2_resource = session.resource('ec2')

    # Get source instance tags
    instance_a = ec2_resource.Instance(src_instance_id)
    instance_a_tags = instance_a.tags

    # Copy the source instance tags to destination instance
    instance_b = ec2_resource.Instance(dst_instance_id)
    instance_b.create_tags(
        DryRun=False,
        Tags=instance_a_tags
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Copy EC2 tags between instances.")
    parser.add_argument(
        '-r',
        '--region',
        action='store',
        dest='region',
        help="AWS Region"
    )
    parser.add_argument(
        '-s',
        '--src',
        action='store',
        dest='src_instance_id',
        help="Source instance ID"
    )
    parser.add_argument(
        '-d',
        '--dest',
        action='store',
        dest='dst_instance_id',
        help="Destination instance ID"
    )
    results = parser.parse_args()

    if not vars(results):
        parser.print_help()
        sys.exit(0)

    copy_tags(results.region, results.src_instance_id, results.dst_instance_id)