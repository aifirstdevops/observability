# observability Through Grafana and Prometheus

Dependecy Packages to Be Installed Before configuring Prometheus

sudo yum install python3*-pip

pip install prometheus-client

sudo wget https://github.com/prometheus/prometheus/releases/download/v2.55.0/prometheus-2.55.0.linux-amd64.tar.gz

sudo tar -xvf prometheus-*.tar.gz

sudo mv prometheus-2.55.0.linux-amd64 prometheus

sudo ./prometheus --config.file=prometheus.yml

Configure grafana.repo in /etc/yum.repos.d/

sudo yum install grafana -y

sudo systemctl daemon-reload

sudo systemctl start grafana-server

sudo systemctl enable grafana-server

mkdir node-exporter

cd node-exporter

NODE_EXPORTER_VERSION=1.8.2

wget https://github.com/prometheus/node_exporter/releases/download/v${NODE_EXPORTER_VERSION}/node_exporter-${NODE_EXPORTER_VERSION}.linux-amd64.tar.gz

tar xvf node_exporter-${NODE_EXPORTER_VERSION}.linux-amd64.tar.gz

sudo mv node_exporter-${NODE_EXPORTER_VERSION}.linux-amd64/node_exporter /usr/local/bin/

sudo useradd --no-create-home --shell /bin/false node_exporter

sudo chown node_exporter:node_exporter /usr/local/bin/node_exporter

sudo tee /etc/systemd/system/node_exporter.service > /dev/null <<EOF
 [Unit]
 Description=Node Exporter
 Wants=network-online.target
 After=network-online.target
[Service]
User=node_exporter
Group=node_exporter
Type=simple
ExecStart=/usr/local/bin/node_exporter   --collector.cpu   --collector.meminfo   --collector.diskstats   --collector.filesystem   --collector.netdev
[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable node_exporter
sudo systemctl start node_exporter


