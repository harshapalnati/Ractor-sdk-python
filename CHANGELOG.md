# Changelog

## 1.0.1 (2025-12-19)

Full Changelog: [v1.0.0...v1.0.1](https://github.com/harshapalnati/Ractor-sdk-python/compare/v1.0.0...v1.0.1)

### Bug Fixes

* **client:** close streams without requiring full consumption ([2d9e199](https://github.com/harshapalnati/Ractor-sdk-python/commit/2d9e1992edc07a298c405489a015ade5321caca4))
* compat with Python 3.14 ([542ae0d](https://github.com/harshapalnati/Ractor-sdk-python/commit/542ae0df81969aa2b7ba4da28b8c93f8398e5b3f))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([f047c07](https://github.com/harshapalnati/Ractor-sdk-python/commit/f047c0747f29bbc4b4f784a89237de191cbfc9d1))
* ensure streams are always closed ([6db694d](https://github.com/harshapalnati/Ractor-sdk-python/commit/6db694d8fd9ed114556e0d24a17ffc5169908784))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([e249045](https://github.com/harshapalnati/Ractor-sdk-python/commit/e2490452e1af6872d3f42bfb859933a0ca4ebbc4))
* use async_to_httpx_files in patch method ([8fc007c](https://github.com/harshapalnati/Ractor-sdk-python/commit/8fc007c3797da74b1a47f956a9c6cd70e801fd2f))


### Chores

* add Python 3.14 classifier and testing ([cbd83f0](https://github.com/harshapalnati/Ractor-sdk-python/commit/cbd83f048d2a27e29f0dfc164a065dc89fd107ed))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([b30a8b5](https://github.com/harshapalnati/Ractor-sdk-python/commit/b30a8b5059d93e4520b050cadb9a8c2652838185))
* **docs:** use environment variables for authentication in code snippets ([10056c4](https://github.com/harshapalnati/Ractor-sdk-python/commit/10056c49ad5cef193106eaa5cbb2f102efd708d6))
* **internal/tests:** avoid race condition with implicit client cleanup ([9732c88](https://github.com/harshapalnati/Ractor-sdk-python/commit/9732c88a6bb4837d3a275a07c0d49f91f12c4f16))
* **internal:** add `--fix` argument to lint script ([57990ad](https://github.com/harshapalnati/Ractor-sdk-python/commit/57990ad8fbd1ccc607cde0427629efdad9cca116))
* **internal:** add missing files argument to base client ([ed6de13](https://github.com/harshapalnati/Ractor-sdk-python/commit/ed6de13a0f82a3f033038b260b8e0936aa6c2035))
* **internal:** grammar fix (it's -&gt; its) ([309be30](https://github.com/harshapalnati/Ractor-sdk-python/commit/309be307f35969baa97033b0f1d6c0d15b23aec2))
* **package:** drop Python 3.8 support ([8ce3733](https://github.com/harshapalnati/Ractor-sdk-python/commit/8ce3733f0acc5e48569f87c3903f55d3b9d27edd))
* speedup initial import ([4d0ff18](https://github.com/harshapalnati/Ractor-sdk-python/commit/4d0ff180969e46aa7e97d531f2acdf3a5b837cca))
* update lockfile ([0a72796](https://github.com/harshapalnati/Ractor-sdk-python/commit/0a72796575e31018931ec31b7a596d4799cfb037))

## 1.0.0 (2025-10-20)

Full Changelog: [v0.0.1...v1.0.0](https://github.com/harshapalnati/Ractor-sdk-python/compare/v0.0.1...v1.0.0)

### Chores

* update SDK settings ([8c2663b](https://github.com/harshapalnati/Ractor-sdk-python/commit/8c2663b20981e2d65f7c4af734f785ad17d5f58c))
* update SDK settings ([35446d3](https://github.com/harshapalnati/Ractor-sdk-python/commit/35446d3ce2c2f19b0550253e75e2422fd44c3912))
