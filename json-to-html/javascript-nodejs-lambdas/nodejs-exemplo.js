const AWS = require('aws-sdk');
const inspector2 = new AWS.Inspector2();
const sns = new AWS.SNS();
const SNSTopicARN = process.env.SNSTopic;

exports.handler = function(event) {

  const paramsInspector = {
    "aggregationType": "PACKAGE",
    "maxResults": 5,
    "aggregationRequest": {
      "packageAggregation": {
        "sortOrder": "DESC",
        "sortBy": "CRITICAL"
      }
    }
  };

  inspector2.listFindingAggregations(paramsInspector, function(err, data) {
    if (err) {
      console.log(err, err.stack)
    } else {
      let msg = 'Vulnerabilities impacting the most instances and images.\n\n';
      data.responses.forEach(pkg => {
        console.log(pkg.packageAggregation);
        msg += 'Package: ' + pkg.packageAggregation.packageName + '\n';
        msg += 'Counts of findings by severity: \n';
        msg += 'Critical = ' + pkg.packageAggregation.severityCounts.critical + '\n';
        msg += 'High = ' + pkg.packageAggregation.severityCounts.high + '\n';
        msg += 'Medium = ' + pkg.packageAggregation.severityCounts.medium + '\n\n';
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
