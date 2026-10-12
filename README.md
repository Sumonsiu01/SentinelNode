# SentinelNode
# SentinelNode 🛡️
### An Agentic AI-Based Self-Healing Framework for Cyber Defence in Containerised Microservices

SentinelNode is a research project that explores how Agentic AI can improve the security and resilience of containerised microservices.

It aims to detect suspicious activity, isolate potentially compromised containers, and restore services automatically. The goal is to reduce incident response time while maintaining service availability.

## 🚀 Key Features

- **Real-Time Monitoring:** Collects application, container, and network telemetry.
- **Anomaly Detection:** Identifies suspicious traffic and unusual resource usage.
- **Agentic AI Reasoning:** Uses a ReAct-based agent to analyse incidents and select response actions.
- **Automated Containment:** Supports controlled traffic draining and container isolation.
- **Self-Healing:** Verifies clean container images, launches replacement containers, and checks service health.
- **Service Recovery:** Restores traffic after recovery checks pass.
- **Performance Evaluation:** Measures detection accuracy, response time, resource overhead, and service availability.

## 🏗️ System Architecture

SentinelNode consists of four main components:

1. **Telemetry and Perception Plane**  
   Collects application logs, Linux cgroup metrics, and network connection data.

2. **Cognitive Reasoning Plane**  
   Uses a ReAct-based AI agent to analyse suspicious events and select appropriate actions.

3. **Actuator and Containment Plane**  
   Applies controlled actions such as traffic draining, network isolation, and container freezing.

4. **Self-Healing Plane**  
   Verifies container images, starts clean replacements, performs health checks, and restores traffic.

## 🛠️ Technologies

- **Programming Languages:** Python, Go
- **AI Agent Framework:** LangGraph
- **Containerisation:** Docker
- **Reverse Proxy:** Nginx
- **Operating System Telemetry:** Linux cgroups v2, Netlink API
- **Communication:** Unix domain sockets, JSON
- **Evaluation:** Python-based metrics and experimental analysis

*The final technology list should reflect the components implemented in the current version.*

## 🎯 Attack Scenarios

The project evaluates its defence approach against three attack scenarios:

- **Layer-7 HTTP Flood:** Generates excessive application-layer requests.
- **Credential Stuffing:** Simulates repeated login attempts using credential combinations.
- **Resource Exhaustion:** Consumes system resources to degrade service performance.

Testing is intended for an isolated environment with controlled attack traffic.

## 📊 Evaluation Metrics

SentinelNode is evaluated using the following metrics:

| Metric | Purpose |
|---|---|
| Mean Time to Detect (MTTD) | Measures how quickly an attack is detected |
| Mean Time to Isolate (MTTI) | Measures how quickly a compromised service is isolated |
| Mean Time to Remediate (MTTR) | Measures the time required to mitigate an incident |
| Precision, Recall and F1-score | Evaluate detection performance |
| Service Availability | Measures the ability to serve legitimate requests |
| CPU and Memory Usage | Measures system overhead |
| Request Success Rate | Evaluates the impact on legitimate traffic |

The evaluation compares SentinelNode with static container restarts and rule-based automation.

## 🔄 Defence Workflow

1. Collect telemetry from application, container, and network layers.
2. Detect suspicious behaviour.
3. Send relevant evidence to the AI reasoning engine.
4. Select an appropriate response using predefined tools and safety checks.
5. Isolate the affected container or drain its traffic.
6. Start a verified replacement container.
7. Check service health.
8. Restore traffic when recovery checks succeed.
9. Record the incident and evaluation metrics.

## 🔒 Security Considerations

SentinelNode is designed around controlled and auditable response actions.

- Validate AI-generated actions against strict schemas.
- Restrict access to privileged container and host controls.
- Verify replacement images before deployment.
- Perform health checks before restoring traffic.
- Keep testing within an authorised, isolated environment.
- Record security events and action outcomes for evaluation.

AI-generated decisions should not bypass the framework's security controls.

## 🧪 Research Methodology

The project follows an experimental approach:

1. Design the SentinelNode architecture.
2. Implement the telemetry, reasoning, containment, and recovery components.
3. Build an isolated containerised test environment.
4. Execute controlled attack scenarios.
5. Compare results against baseline defence approaches.
6. Analyse response time, detection performance, resource overhead, and service availability.

## 📌 Project Status

**Status:** Research prototype / experimental development.

SentinelNode is being developed and evaluated as part of an MSc Cyber Security Management research project. Its effectiveness and limitations are assessed through controlled experiments.

## 🔮 Future Improvements

- Support for Kubernetes-based environments.
- More robust anomaly detection.
- Improved agent decision validation.
- Enhanced audit logging and incident reporting.
- Evaluation against additional attack scenarios.
- Further optimisation of AI reasoning latency and resource usage.

## ⚠️ Disclaimer

SentinelNode is intended for academic research and authorised security testing. Attack simulations should only be performed in controlled environments where testing is explicitly permitted.

## 👨‍💻 Author

**Sumon Ahmed**

MSc Cyber Security Management  
Aston University, London

## 📄 License

A licence has not yet been specified. Add a suitable licence before distributing the project for reuse.
