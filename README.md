# Pi-hole-Influx

A simple daemonized and dockerized script to report Pi-Hole stats to an InfluxDB, ready to be displayed via Grafana.

![Example Grafana Dashboard](.readme-assets/dashboard.png)

## Requirements and Setup

The container need following values to function

* `INFLUX_HOST`
* `INFLUX_PORT`
* `INFLUX_USERNAME`
* `INFLUX_PASSWORD`
* `INFLUX_DATABASE`
* `PIHOLE_API`
* `PIHOLE_INSTANCE_NAME`
* `REPORTING_INTERVAL`

Example command:

```
docker run --rm -t -i -e INFLUX_HOST="influx" \
-e INFLUX_PORT="8086" \
-e INFLUX_USERNAME="foo" \
-e INFLUX_PASSWORD="bar" \
-e INFLUX_DATABASE="pihole" \
-e PIHOLE_API="http://pihole/admin/api.php" \
-e PIHOLE_INSTANCE_NAME="pihole" \
-e REPORTING_INTERVAL="10" \
xoryouyou/pi-hole-influx
```

## Set up a Grafana Dashboard 

The example dashboard seen [at the top](#pi-hole-influx) uses the collected data and displays it in concise and sensible graphs and single stats. The dashboard can be imported into your Grafana instance from the `dashboard.json` file included in the repo, or by using ID `6603` to [import it from Grafana's Dashboard Directory](https://grafana.com/dashboards/6603).


## Attributions

The script originally [created by Jon Hayward](https://fattylewis.com/Graphing-pi-hole-stats/), adapted to work with InfluxDB [by /u/tollsjo in December 2016](https://github.com/sco01/piholestatus), and [improved and extended by @johnappletree](https://github.com/johnappletree/piholestatus). "If I have seen further it is by standing on the shoulders of giants". 🤓
