#!/usr/bin/env node
const i2c     = require('i2c-bus');
const util    = require('util');
const fs      = require('fs');
const ms = 5000;               // Repeat time
const mqtt = require('mqtt');
const client = mqtt.connect('mqtt://mqtt.thingspeak.com');

const bus = 2;
const tmp101 = [0x48];
const sensor = i2c.openSync(bus);

const filename = "/home/debian/exercises/iot/thingspeak/keys_office.json";
const keys = JSON.parse(fs.readFileSync(filename));
const url = "channels/" + keys.channel_id + "/publish/" + keys.write_key;

for(var i=0; i<tmp101.length; i++) {
  const CMD_ADDR = 0x1;
  sensor.writeByteSync(tmp101[i], CMD_ADDR, 0x60);  // 12-bit mode
}

client.on('connect', function() {
  var tempOld = [];
  var temp = [];
  var tempC = 0;
  var tempF = 0;

    setInterval(readWeather, ms);
    function readWeather(data) {

        for(var i=0; i<tmp101.length; i++) {
            temp[i] = sensor.readWordSync(tmp101[i], 0x0);    // Read temp
            tempC = (((temp[i] & 0xff) << 8) | ((temp[i] & 0xff00) >> 8))/256;
            tempF = tempC*1.8+32;     //Convert to F
            console.log("temp: %dF (0x%s)", temp[i], tmp101[i].toString(16));
        }
        if((temp[0] !== tempOld[0])) {
          client.publish(url, util.format("field1=%s", temp[0]));
          tempOld[0] = temp[0];
        }
    }
});
