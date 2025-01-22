# Configuration Options #

This document provides a tabular overview of the configuration options available in the `uvicorn_configurable` module.
For clarity, the division into subsections as done in the [uvicorn documentation](https://www.uvicorn.org/settings/)
is followed here as well. The description of the options is taken from the 
[uvicorn documentation](https://www.uvicorn.org/settings/), with minor modifications where needed.

## Application

| **Option** | **Type** | **Default** | **Description** |
|------------|----------|-------------|------------------|
| app        | str      | ""          | The ASGI application to run, in the format `<module>:<attribute>`. Set to `""` if supplying the app instance. |
| factory    | bool     | False       | Whether to treat `app` as an application factory, i.e., a `() -> <ASGI app>` callable. |

## SocketBinding

| **Option** | **Type** | **Default** | **Description** |
|------------|----------|-------------|------------------|
| host       | str      | "127.0.0.1" | Bind socket to this host. Use `'0.0.0.0'` to make the application available on your local network. |
| port       | int      | 8000        | Bind to a socket with this port. |
| uds        | str      | ""          | Bind to a UNIX domain socket, e.g., `'/tmp/uvicorn.sock'`. |
| fd         | int      | -1          | Bind to socket from this file descriptor. |

## Development

| **Option**         | **Type**     | **Default** | **Description** |
|---------------------|--------------|-------------|------------------|
| reload             | bool         | False       | Whether to enable auto-reload. |
| reload_dirs        | list[str]    | []          | Directories to watch for Python file changes. Default: empty list, which implies to watch the current directory. |

## Production

| **Option** | **Type** | **Default** | **Description** |
|------------|----------|-------------|------------------|
| workers    | int      | 0           | Number of worker processes. Defaults to environment variable `$WEB_CONCURRENCY` or 1. |

## Logging

| **Option**           | **Type** | **Default** | **Description** |
|-----------------------|----------|-------------|------------------|
| set_default_log_config | bool     | True        | Whether to use the default  log configuration. |
| log_config            | str      | ""          | Logging configuration file. Supports `dictConfig()` formats (.json, .yaml). |
| log_level             | str      | "info"      | Log level (`'critical'`, `'error'`, `'warning'`, `'info'`, `'debug'`, `'trace'`). |
| access_log            | bool     | True        | Whether to enable an access log without changing the log level. |
| use_colors            | int      | -1          | Enable/disable colorized log formatting. |

## Implementation

| **Option**                  | **Type** | **Default** | **Description** |
|-----------------------------|----------|-------------|------------------|
| loop                       | str      | "auto"      | Event loop implementation (`'auto'`, `'asyncio'`, `'uvloop'`). |
| http                       | str      | "auto"      | HTTP protocol implementation (`'auto'`, `'h11'`, `'httptools'`). |
| ws                         | str      | "auto"      | WebSocket protocol implementation (`'auto'`, `'none'`, `'websockets'`, `'wsproto'`). |
| ws_max_size                | int      | 16777216    | Max WebSocket message size in bytes. |
| ws_max_queue               | int      | 32          | Max WebSocket incoming message queue length. |
| ws_ping_interval           | float    | 20.0        | WebSocket ping interval in seconds. |
| ws_ping_timeout            | float    | 20.0        | WebSocket ping timeout in seconds. |
| lifespan                   | str      | "auto"      | Lifespan protocol implementation (`'auto'`, `'on'`, `'off'`). |
| h11_max_incomplete_event_size | int    | 16384       | Max bytes for buffering an incomplete event (h11). |

## ApplicationInterface

| **Option**  | **Type** | **Default** | **Description** |
|-------------|----------|-------------|------------------|
| interface   | str      | "auto"      | Select ASGI3, ASGI2, or WSGI as the application interface. |

## HTTP

| **Option**                | **Type**    | **Default** | **Description** |
|---------------------------|-------------|-------------|------------------|
| root_path                | str         | ""          | ASGI root path for submounted applications. |
| proxy_headers            | bool        | True        | Enable `X-Forwarded-*` headers for remote address info. |
| set_default_forwarded_allow_ips | bool | True        | Use the  default for `forwarded_allow_ips`. |
| forwarded_allow_ips      | list[str]   | []          | Trusted IPs for proxy headers. |
| server_header            | bool        | True        | Enable the default `Server` header. |
| date_header              | bool        | True        | Enable the default `Date` header. |

## HTTPS

| **Option**         | **Type** | **Default**              | **Description** |
|---------------------|----------|--------------------------|------------------|
| ssl_keyfile        | str      | ""                       | SSL key file path. |
| ssl_keyfile_password | str    | ""                       | Password for SSL key. |
| ssl_certfile       | str      | ""                       | SSL certificate file. |
| ssl_version        | int      | ssl.PROTOCOL_TLS_SERVER  | SSL version. |
| ssl_cert_reqs      | int      | ssl.CERT_NONE            | Whether client certificates are required. |
| ssl_ca_certs       | str      | ""                       | CA certificates file path. |
| ssl_ciphers        | str      | "TLSv1"                  | Ciphers to use. |

## ResourceLimits

| **Option**         | **Type** | **Default** | **Description** |
|---------------------|----------|-------------|------------------|
| limit_concurrency  | int      | -1          | Max concurrent connections/tasks. |
| limit_max_requests | int      | -1          | Max requests before terminating the process. |
| backlog            | int      | 2048        | Max connections to hold in backlog. |

## Timeouts

| **Option**                  | **Type** | **Default** | **Description** |
|-----------------------------|----------|-------------|------------------|
| timeout_keep_alive          | int      | 5           | Close Keep-Alive connections after timeout (seconds). |
| timeout_graceful_shutdown   | int      | -1          | Max seconds for graceful shutdown before termination. |

## Uvicorn

Collects all of the above sections.

| **Section**              | **Type**                               | **Default** | **Description** |
|--------------------------|----------------------------------------|-------------|------------------|
| application              | UvicornApplicationConfigSection       | default instance | See [Application](#application). |
| socket_binding           | UvicornSocketBindingConfigSection     | default instance | See [SocketBinding](#socketbinding). |
| development              | UvicornDevelopmentConfigSection       | default instance | See [Development](#development). |
| production               | UvicornProductionConfigSection        | default instance | See [Production](#production). |
| logging                  | UvicornLoggingConfigSection           | default instance | See [Logging](#logging). |
| implementation           | UvicornImplementationConfigSection    | default instance | See [Implementation](#implementation). |
| application_interface    | UvicornApplicationInterfaceConfigSection | default instance | See [ApplicationInterface](#applicationinterface). |
| http                     | UvicornHTTPConfigSection              | default instance | See [HTTP](#http). |
| https                    | UvicornHTTPSConfigSection             | default instance | See [HTTPS](#https). |
| resource_limits          | UvicornResourceLimitsConfigSection    | default instance | See [ResourceLimits](#resourcelimits). |
| timeouts                 | UvicornTimeoutsConfigSection          | default instance | See [Timeouts](#timeouts). |
