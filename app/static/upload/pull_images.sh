#!/usr/bin/env bash
echo "pull image start"

echo "pull image pgsql"
sudo docker pull paunin/postdock-pgsql

echo "pull image pgpool"
sudo docker pull paunin/postdock-pgpool

echo "pull image nsq"
sudo docker pull nsqio/nsq

echo "pull image visalizer"
sudo docker pull dockersamples/visualizer

echo "pull image tutum/influxdb:0.8.8"
sudo docker pull tutum/influxdb:0.8.8

echo "pull image google/cadvisor"
sudo docker pull google/cadvisor

echo "pull image grafana/grafana"
sudo docker pull grafana/grafana

echo "pull image redis"
sudo docker pull reids

echo "pull image golang"
sudo docker pull golang

echo "pull image python"
sudo docker pull python

echo "pull image php"
sudo docker pull php:7.1-apache

echo "pull image finish"
