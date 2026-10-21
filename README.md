<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/header-mobile-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/header-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <img src="assets/header-light.svg" width="100%" alt="Java Full Stack — from browser to backend.">
</picture>

# Aleksandr Kashevarov

**Java Full Stack Developer** · Backend systems, browser applications & open source.

I build applications across the stack: Java services, React interfaces, and the infrastructure connecting them. My focus is on streaming data, real-time communication, and making failure handling explicit.

### What I work with

**Backend**  
Java · Spring Boot · Spring WebFlux · Kafka · PostgreSQL · Redis

**Frontend**  
TypeScript · React · Browser Streams · Server-Sent Events

**Infrastructure**  
Docker · Kubernetes · S3-compatible storage · Observability

### Building in the open

I'm turning recurring application problems into focused, reusable libraries. These projects are in early development; their repositories describe the planned APIs and release criteria.

#### [browser-media-cache](https://github.com/59Alex/browser-media-cache)

**TypeScript · Browser infrastructure**  
Shared media loads, explicit ownership of blob URLs, and predictable cache cleanup. Designed to keep resource lifetimes manageable when several components use the same media.

#### [s3-file-streams](https://github.com/59Alex/s3-file-streams)

**Java + TypeScript · Streaming**  
Continuous file transfer from the browser through Java to S3 — and back. The goal: bounded buffering, backpressure, cancellation, and clear completion semantics across the whole pipeline.

#### [browser-sse-relay](https://github.com/59Alex/browser-sse-relay)

**TypeScript · Real-time delivery**  
Recovering event streams after a disconnect: cursors, replay, and an explicit resync path when history is no longer available. Built around a documented client–server contract.

---

**How I approach engineering**  
Clear contracts. Visible failure modes. Reproducible tests. Useful documentation.

Have a use case for one of these libraries? Open an issue in its repository — concrete scenarios help shape the API.
