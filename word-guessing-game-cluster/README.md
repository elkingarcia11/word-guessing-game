## 🏗 Hosting with Kubernetes

To host the Word Guessing Game using kubernetes, follow these steps:
1. Install Kubectl with Homebrew on macOS:
```bash
   brew install kubectl
   ```
or
```bash
   brew install kubernetes-cli
   ```
2. Test installation with the command below to ensure that your installation is working correctly:
```bash
   kubectl version --client
   ```

3. Navigate to the cluster folder
   ```bash
   cd word-guessing-game-cluster
   ```

2. Create a deployment object using the YAML file below:
   ```bash
   kubectl apply -f nginx-deployment.yaml
   ```
