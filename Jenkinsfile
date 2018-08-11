#!/usr/bin/env groovy
import hudson.model.*
import hudson.EnvVars
import groovy.json.JsonSlurperClassic
import groovy.json.JsonBuilder
import groovy.json.JsonOutput
import java.net.URL

try {
node {
stage '\u2776 Stage 1'
echo "\u2600 BUILD_URL=${env.BUILD_URL}"
def workspace = pwd()
echo "\u2600 workspace=${workspace}"
stage '\u2777 stage 2'
} 
}
catch(exc){

err = caughtError
currentBuild.Result = "FAILURE"
}
if (err) {
     throw err
 }

