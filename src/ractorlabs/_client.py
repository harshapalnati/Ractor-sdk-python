# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, RactorlabsError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import auth, version, sessions, blocklist, operators, published, responses
    from .resources.auth import AuthResource, AsyncAuthResource
    from .resources.version import VersionResource, AsyncVersionResource
    from .resources.blocklist import BlocklistResource, AsyncBlocklistResource
    from .resources.operators import OperatorsResource, AsyncOperatorsResource
    from .resources.responses import ResponsesResource, AsyncResponsesResource
    from .resources.sessions.sessions import SessionsResource, AsyncSessionsResource
    from .resources.published.published import PublishedResource, AsyncPublishedResource

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Ractorlabs",
    "AsyncRactorlabs",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "http://localhost:9000/api/v0",
    "environment_1": "https://{host}/api/v0",
}


class Ractorlabs(SyncAPIClient):
    # client options
    api_key: str
    host: str

    _environment: Literal["production", "environment_1"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        host: str | None = None,
        environment: Literal["production", "environment_1"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Ractorlabs client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `RACTORLABS_API_KEY`
        - `host` from `RACTORLABS_HOST`
        """
        if api_key is None:
            api_key = os.environ.get("RACTORLABS_API_KEY")
        if api_key is None:
            raise RactorlabsError(
                "The api_key client option must be set either by passing api_key to the client or by setting the RACTORLABS_API_KEY environment variable"
            )
        self.api_key = api_key

        if host is None:
            host = os.environ.get("RACTORLABS_HOST") or "api.example.com"
        self.host = host

        self._environment = environment

        base_url_env = os.environ.get("RACTORLABS_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `RACTORLABS_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def version(self) -> VersionResource:
        from .resources.version import VersionResource

        return VersionResource(self)

    @cached_property
    def operators(self) -> OperatorsResource:
        from .resources.operators import OperatorsResource

        return OperatorsResource(self)

    @cached_property
    def published(self) -> PublishedResource:
        from .resources.published import PublishedResource

        return PublishedResource(self)

    @cached_property
    def auth(self) -> AuthResource:
        from .resources.auth import AuthResource

        return AuthResource(self)

    @cached_property
    def blocklist(self) -> BlocklistResource:
        from .resources.blocklist import BlocklistResource

        return BlocklistResource(self)

    @cached_property
    def sessions(self) -> SessionsResource:
        from .resources.sessions import SessionsResource

        return SessionsResource(self)

    @cached_property
    def responses(self) -> ResponsesResource:
        from .resources.responses import ResponsesResource

        return ResponsesResource(self)

    @cached_property
    def with_raw_response(self) -> RactorlabsWithRawResponse:
        return RactorlabsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RactorlabsWithStreamedResponse:
        return RactorlabsWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        host: str | None = None,
        environment: Literal["production", "environment_1"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            host=host or self.host,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncRactorlabs(AsyncAPIClient):
    # client options
    api_key: str
    host: str

    _environment: Literal["production", "environment_1"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        host: str | None = None,
        environment: Literal["production", "environment_1"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncRactorlabs client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `RACTORLABS_API_KEY`
        - `host` from `RACTORLABS_HOST`
        """
        if api_key is None:
            api_key = os.environ.get("RACTORLABS_API_KEY")
        if api_key is None:
            raise RactorlabsError(
                "The api_key client option must be set either by passing api_key to the client or by setting the RACTORLABS_API_KEY environment variable"
            )
        self.api_key = api_key

        if host is None:
            host = os.environ.get("RACTORLABS_HOST") or "api.example.com"
        self.host = host

        self._environment = environment

        base_url_env = os.environ.get("RACTORLABS_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `RACTORLABS_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def version(self) -> AsyncVersionResource:
        from .resources.version import AsyncVersionResource

        return AsyncVersionResource(self)

    @cached_property
    def operators(self) -> AsyncOperatorsResource:
        from .resources.operators import AsyncOperatorsResource

        return AsyncOperatorsResource(self)

    @cached_property
    def published(self) -> AsyncPublishedResource:
        from .resources.published import AsyncPublishedResource

        return AsyncPublishedResource(self)

    @cached_property
    def auth(self) -> AsyncAuthResource:
        from .resources.auth import AsyncAuthResource

        return AsyncAuthResource(self)

    @cached_property
    def blocklist(self) -> AsyncBlocklistResource:
        from .resources.blocklist import AsyncBlocklistResource

        return AsyncBlocklistResource(self)

    @cached_property
    def sessions(self) -> AsyncSessionsResource:
        from .resources.sessions import AsyncSessionsResource

        return AsyncSessionsResource(self)

    @cached_property
    def responses(self) -> AsyncResponsesResource:
        from .resources.responses import AsyncResponsesResource

        return AsyncResponsesResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncRactorlabsWithRawResponse:
        return AsyncRactorlabsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRactorlabsWithStreamedResponse:
        return AsyncRactorlabsWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        host: str | None = None,
        environment: Literal["production", "environment_1"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            host=host or self.host,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class RactorlabsWithRawResponse:
    _client: Ractorlabs

    def __init__(self, client: Ractorlabs) -> None:
        self._client = client

    @cached_property
    def version(self) -> version.VersionResourceWithRawResponse:
        from .resources.version import VersionResourceWithRawResponse

        return VersionResourceWithRawResponse(self._client.version)

    @cached_property
    def operators(self) -> operators.OperatorsResourceWithRawResponse:
        from .resources.operators import OperatorsResourceWithRawResponse

        return OperatorsResourceWithRawResponse(self._client.operators)

    @cached_property
    def published(self) -> published.PublishedResourceWithRawResponse:
        from .resources.published import PublishedResourceWithRawResponse

        return PublishedResourceWithRawResponse(self._client.published)

    @cached_property
    def auth(self) -> auth.AuthResourceWithRawResponse:
        from .resources.auth import AuthResourceWithRawResponse

        return AuthResourceWithRawResponse(self._client.auth)

    @cached_property
    def blocklist(self) -> blocklist.BlocklistResourceWithRawResponse:
        from .resources.blocklist import BlocklistResourceWithRawResponse

        return BlocklistResourceWithRawResponse(self._client.blocklist)

    @cached_property
    def sessions(self) -> sessions.SessionsResourceWithRawResponse:
        from .resources.sessions import SessionsResourceWithRawResponse

        return SessionsResourceWithRawResponse(self._client.sessions)

    @cached_property
    def responses(self) -> responses.ResponsesResourceWithRawResponse:
        from .resources.responses import ResponsesResourceWithRawResponse

        return ResponsesResourceWithRawResponse(self._client.responses)


class AsyncRactorlabsWithRawResponse:
    _client: AsyncRactorlabs

    def __init__(self, client: AsyncRactorlabs) -> None:
        self._client = client

    @cached_property
    def version(self) -> version.AsyncVersionResourceWithRawResponse:
        from .resources.version import AsyncVersionResourceWithRawResponse

        return AsyncVersionResourceWithRawResponse(self._client.version)

    @cached_property
    def operators(self) -> operators.AsyncOperatorsResourceWithRawResponse:
        from .resources.operators import AsyncOperatorsResourceWithRawResponse

        return AsyncOperatorsResourceWithRawResponse(self._client.operators)

    @cached_property
    def published(self) -> published.AsyncPublishedResourceWithRawResponse:
        from .resources.published import AsyncPublishedResourceWithRawResponse

        return AsyncPublishedResourceWithRawResponse(self._client.published)

    @cached_property
    def auth(self) -> auth.AsyncAuthResourceWithRawResponse:
        from .resources.auth import AsyncAuthResourceWithRawResponse

        return AsyncAuthResourceWithRawResponse(self._client.auth)

    @cached_property
    def blocklist(self) -> blocklist.AsyncBlocklistResourceWithRawResponse:
        from .resources.blocklist import AsyncBlocklistResourceWithRawResponse

        return AsyncBlocklistResourceWithRawResponse(self._client.blocklist)

    @cached_property
    def sessions(self) -> sessions.AsyncSessionsResourceWithRawResponse:
        from .resources.sessions import AsyncSessionsResourceWithRawResponse

        return AsyncSessionsResourceWithRawResponse(self._client.sessions)

    @cached_property
    def responses(self) -> responses.AsyncResponsesResourceWithRawResponse:
        from .resources.responses import AsyncResponsesResourceWithRawResponse

        return AsyncResponsesResourceWithRawResponse(self._client.responses)


class RactorlabsWithStreamedResponse:
    _client: Ractorlabs

    def __init__(self, client: Ractorlabs) -> None:
        self._client = client

    @cached_property
    def version(self) -> version.VersionResourceWithStreamingResponse:
        from .resources.version import VersionResourceWithStreamingResponse

        return VersionResourceWithStreamingResponse(self._client.version)

    @cached_property
    def operators(self) -> operators.OperatorsResourceWithStreamingResponse:
        from .resources.operators import OperatorsResourceWithStreamingResponse

        return OperatorsResourceWithStreamingResponse(self._client.operators)

    @cached_property
    def published(self) -> published.PublishedResourceWithStreamingResponse:
        from .resources.published import PublishedResourceWithStreamingResponse

        return PublishedResourceWithStreamingResponse(self._client.published)

    @cached_property
    def auth(self) -> auth.AuthResourceWithStreamingResponse:
        from .resources.auth import AuthResourceWithStreamingResponse

        return AuthResourceWithStreamingResponse(self._client.auth)

    @cached_property
    def blocklist(self) -> blocklist.BlocklistResourceWithStreamingResponse:
        from .resources.blocklist import BlocklistResourceWithStreamingResponse

        return BlocklistResourceWithStreamingResponse(self._client.blocklist)

    @cached_property
    def sessions(self) -> sessions.SessionsResourceWithStreamingResponse:
        from .resources.sessions import SessionsResourceWithStreamingResponse

        return SessionsResourceWithStreamingResponse(self._client.sessions)

    @cached_property
    def responses(self) -> responses.ResponsesResourceWithStreamingResponse:
        from .resources.responses import ResponsesResourceWithStreamingResponse

        return ResponsesResourceWithStreamingResponse(self._client.responses)


class AsyncRactorlabsWithStreamedResponse:
    _client: AsyncRactorlabs

    def __init__(self, client: AsyncRactorlabs) -> None:
        self._client = client

    @cached_property
    def version(self) -> version.AsyncVersionResourceWithStreamingResponse:
        from .resources.version import AsyncVersionResourceWithStreamingResponse

        return AsyncVersionResourceWithStreamingResponse(self._client.version)

    @cached_property
    def operators(self) -> operators.AsyncOperatorsResourceWithStreamingResponse:
        from .resources.operators import AsyncOperatorsResourceWithStreamingResponse

        return AsyncOperatorsResourceWithStreamingResponse(self._client.operators)

    @cached_property
    def published(self) -> published.AsyncPublishedResourceWithStreamingResponse:
        from .resources.published import AsyncPublishedResourceWithStreamingResponse

        return AsyncPublishedResourceWithStreamingResponse(self._client.published)

    @cached_property
    def auth(self) -> auth.AsyncAuthResourceWithStreamingResponse:
        from .resources.auth import AsyncAuthResourceWithStreamingResponse

        return AsyncAuthResourceWithStreamingResponse(self._client.auth)

    @cached_property
    def blocklist(self) -> blocklist.AsyncBlocklistResourceWithStreamingResponse:
        from .resources.blocklist import AsyncBlocklistResourceWithStreamingResponse

        return AsyncBlocklistResourceWithStreamingResponse(self._client.blocklist)

    @cached_property
    def sessions(self) -> sessions.AsyncSessionsResourceWithStreamingResponse:
        from .resources.sessions import AsyncSessionsResourceWithStreamingResponse

        return AsyncSessionsResourceWithStreamingResponse(self._client.sessions)

    @cached_property
    def responses(self) -> responses.AsyncResponsesResourceWithStreamingResponse:
        from .resources.responses import AsyncResponsesResourceWithStreamingResponse

        return AsyncResponsesResourceWithStreamingResponse(self._client.responses)


Client = Ractorlabs

AsyncClient = AsyncRactorlabs
