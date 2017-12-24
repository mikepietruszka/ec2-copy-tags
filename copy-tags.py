#!/usr/bin/env python

import boto3
import sys

try:
    session = boto3.session.Session(region_name='us-west-2')
except:
    raise Exception("ERROR: error")
else:    
    ec2_client = session.client('ec2')
    ec2_resource = session.resource('ec2')

instance_a_id = sys.argv[1]
instance_b_id = sys.argv[2]

# Get source instance tags
instance_a = ec2_resource.Instance(instance_a_id)
instance_a_tags = instance_a.tags

# Copy the source instance tags to destination instance
instance_b = ec2_resource.Instance(instance_b_id)
instance_b.create_tags(
    DryRun=False,
    Tags=instance_a_tags
)

