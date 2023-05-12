const AWS = require('aws-sdk');
const inspector2 = new AWS.Inspector2();
const sns = new AWS.SNS();
const SNSTopicARN = process.env.SNSTopic;

exports.handler = function(event) {

  const paramsInspector = {
    "aggregationType": "AWS_EC2_INSTANCE",
    "maxResults": 25,
    "aggregationRequest": {
        "ec2InstanceAggregation": {
          "sortBy": "ALL",
          "instanceTags": [{
              "comparison": "EQUALS",
              "key": "DevOpsRelatorioAmazonInspector",
              "value": '1'
          }]
        }
      }
  };

  inspector2.listFindingAggregations(paramsInspector, function(err, data) {
    if (err) {
      console.log(err, err.stack)
    } else {
      let msg = 'Vulnerabilities impacting the most instances and images.\n\n';
      data.responses.forEach(instance => {
        console.log(instance.ec2InstanceAggregation);
        msg += 'EC2 Instance ID: ' + instance.ec2InstanceAggregation.instanceId + '\n';
        msg += 'Counts of findings by severity: \n';
        msg += 'Critical = ' + instance.ec2InstanceAggregation.severityCounts.critical + '\n';
        msg += 'High = ' + instance.ec2InstanceAggregation.severityCounts.high + '\n';
        msg += 'Medium = ' + instance.ec2InstanceAggregation.severityCounts.medium + '\n\n';
      });
      sns.publish({
        TopicArn: SNSTopicARN,
        Subject: 'Weekly Vulnerability Report',
        Message: msg
      }, function(err, data) {
        if (err) console.log(err, err.stack);
        else     console.log(data);
      });
    }
  });
};
