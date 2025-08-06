# observability Through Grafana and Prometheus

Dependecy Packages to Be Installed Before configuring Prometheus

sudo yum install python3*-pip

pip install prometheus-client

sudo wget https://github.com/prometheus/prometheus/releases/download/v2.55.0/prometheus-2.55.0.linux-amd64.tar.gz

sudo tar -xvf prometheus-*.tar.gz

sudo mv prometheus-2.55.0.linux-amd64 prometheus

sudo ./prometheus --config.file=prometheus.yml

sudo tee /etc/yum.repos.d/grafana.repo <<EOF
     [grafana]
     name=grafana
     baseurl=https://packages.grafana.com/oss/rpm
     repo_gpgcheck=1
     enabled=1
     gpgcheck=1
     gpgkey=https://packages.grafana.com/gpg.key
   EOF

sudo yum install grafana -y
sudo systemctl daemon-reload
sudo systemctl start grafana-server
sudo systemctl enable grafana-server


