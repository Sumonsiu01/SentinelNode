# SentinelNode
### An Agentic AI-Based Self-Healing Framework for Cyber Defence in Containerised Microservices

SentinelNode is a research project that explores how agentic AI can support automated threat detection, containment, and service recovery in containerised microservices.

The framework aims to identify suspicious activity, assess potential threats, isolate affected services, and restore service availability while reducing the need for manual intervention.

## Project Objectives

- Detect suspicious traffic and resource usage.
- Analyse potential attacks using an agent-based reasoning approach.
- Isolate compromised or overloaded containers.
- Support service recovery through verified container images.
- Reduce detection and remediation times.
- Maintain service availability during security incidents.

## Proposed Architecture

SentinelNode is organised into four main planes.

### 1. Telemetry and Perception Plane
Collects application logs and container resource metrics. Statistical filtering, such as an Exponentially Weighted Moving Average (EWMA), helps identify unusual activity.

### 2. Cognitive Reasoning Plane
Uses an agent-based reasoning approach to assess detected anomalies and select appropriate response actions. The design explores Python, LangGraph, and structured tool interfaces.

### 3. Actuation and Isolation Plane
Coordinates containment actions, such as network isolation and traffic rerouting, through container and network management tools.

### 4. Self-Healing Plane
Supports recovery by replacing affected instances with verified images, checking service health, and restoring traffic when the replacement is ready.

## Technology Stack

- **Programming Languages:** Python, Go, JavaScript
- **Backend:** Node.js, Express
- **Containerisation:** Docker, Docker Compose
- **Reverse Proxy:** Nginx
- **Agent Framework:** LangGraph
- **Monitoring:** Application logs, container metrics, EWMA-based anomaly detection
- **Security Controls:** Network isolation, resource limits, image verification
- **Testing:** Python, Locust, HTTP-based workload simulation

*The listed technologies describe the project design and intended test environment. Actual implementation status may vary by component.*

## Attack Scenarios

The research considers three main scenarios:

1. **Layer-7 HTTP Flood:** Computationally expensive requests increase CPU usage and reduce service responsiveness.
2. **Credential Stuffing:** Repeated login attempts create unusual authentication failure patterns.
3. **Resource Exhaustion:** Intensive requests increase container resource consumption and may affect service availability.

All security experiments should be conducted in an isolated, authorised test environment.

## Evaluation Metrics

The framework is intended to be evaluated using:

- **Mean Time to Detect (MTTD):** Time required to detect an attack.
- **Mean Time to Isolate (MTTI):** Time required to complete containment.
- **Mean Time to Recover (MTTR):** Time required to restore service.
- **Detection Performance:** Precision, recall, and F1-score.
- **Service Availability:** Successful requests, HTTP errors, and response latency.
- **Resource Overhead:** CPU and memory consumption during monitoring and response.

## Research Goals

The evaluation compares SentinelNode's proposed approach with container-restart strategies and rule-based security automation. The aim is to assess whether agent-based reasoning and progressive containment can improve response time while maintaining service availability.

Performance claims will be based on recorded experimental results rather than assumed outcomes.

## Project Status

SentinelNode is an academic cybersecurity research project. Its architecture and evaluation plan focus on automated threat detection, containment, and recovery in containerised microservices.

Features should be considered implemented only when supported by working code and test evidence.

## Safety and Ethical Considerations

The framework is designed for controlled research and authorised testing. Attack simulations should remain within an isolated testbed and must not target public services or third-party systems.

## Author

**Sumon Ahmed**

MSc Cyber Security Management  
Aston University

## Licence

Add a licence before distributing or reusing this project publicly.
