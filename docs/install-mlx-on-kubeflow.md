# Deploy MLX on an Existing Kubeflow Cluster

To deploy MLX on an existing Kubeflow 1.3.0 Cluster, we can simply use the kustomize plugin that comes with `kubectl` client on v1.17+. Clone the [MLX](https://github.com/machine-learning-exchange/mlx) repo and run the following commands based on your Kubeflow setup.

```shell
git clone https://github.com/machine-learning-exchange/mlx
cd mlx
```

- Deploy MLX on Kubeflow (With OIDC and Istio Mutual Auth)
```shell
kubectl apply -k manifests/istio-auth
```

Then access the MLX page using `http://<Kubeflow_Endpoint>/mlx/`


## Replacing Kubeflow Central Dashboard with MLX Dashboard

To deploy MLX on Kubeflow (With OIDC and Istio Mutual Auth) and replace Kubeflow Central Dashboard with MLX Dashboard, run the following commands:

```shell
git clone https://github.com/machine-learning-exchange/mlx
cd mlx
```

- Deploy MLX on Kubeflow (With OIDC and Istio Mutual Auth)
```shell
kubectl apply -k manifests/prod-multi-user
```

Then access the MLX page using `http://<Kubeflow_Endpoint>/`
