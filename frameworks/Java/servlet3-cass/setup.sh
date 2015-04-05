#!/bin/bash
export JAVA_HOME=/usr/lib/jvm/java-1.7.0-openjdk-amd64
export RESIN_HOME=${IROOT}/resin-4.0.41

sed -i 's|localhost|'"${DBHOST}"'|g' src/main/resources/application.properties

mvn clean compile war:war
rm -rf $RESIN_HOME/webapps/*
cp target/servlet3-cass.war $RESIN_HOME/webapps
$RESIN_HOME/bin/resinctl start