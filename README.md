# External DNS PiHole

Disclaimer: This application is in alpha and is just for home-lab / playing around with.

This application is similar to [external-dns](https://github.com/kubernetes-sigs/external-dns/) in functionality, with support for PiHole application using the DNS server ability.

The application will listen to ingress events in the kubernetes cluster and will send requests to create new DNS records using another application called [pihole-dns-updater](https://github.com/Pobek/pihole-dns-updater). Furthermore, the application will periodically search for DNS records that exists in PiHole but dont exists in kubernetes and will remove them from PiHole if a condition is applied (Same domain with same endpoint IP address).

## Getting Started

### Installation

1. To install, either clone this project or copy the file `example/external-dns-pihole.yaml` file
2. Edit the values of the environment variables in the file
3. Apply if onto kubernetes

```bash
kubectl apply -f example/external-dns-pihole.yaml
```