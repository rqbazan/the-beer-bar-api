# Clean Architecture

Date: 2024-08-04

## Context

Based on the challenge, the idea is to create a system that can be easily maintained and scaled. The system should be able to be easily tested and have a clear separation of concerns.

## Decision

The system will be based on the Clean Architecture. The system will be divided into layers, each layer with its own responsibilities. The layers will be:

![Clean Architecture](/docs/images/archi_folders.png)

- **Domain**: This layer will contain the data structures of the system and the interfaces that will be used by the other layers.

- **Use Cases**: This layer will contain the business rules of the system. For instance, `create_order`, `get_order`, `update_order`, etc.

- **Adapters**: This layer will contain the implementation of the interfaces defined in the domain ports, as well as the REST API application which is a entry point of the system.

## Consequences

- The system will be easier to maintain and scale.
- The system will be easier to test.
- The system will have a clear separation of concerns.
