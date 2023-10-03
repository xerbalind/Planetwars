FROM rust:1.72 AS build-env


WORKDIR /sources

RUN git clone https://github.com/rustwasm/wasm-pack
WORKDIR wasm-pack

RUN rustup default stable
RUN cargo install --path .


WORKDIR /planetwars
COPY . .

WORKDIR backend
RUN cargo build --release


WORKDIR ../frontend

RUN cargo update
RUN wasm-pack build

FROM node:20
COPY --from=build-env /planetwars /planetwars
WORKDIR /planetwars/frontend/www
RUN npm install
RUN npm run build

WORKDIR /planetwars/backend

EXPOSE 9142
EXPOSE 8000
EXPOSE 3012

CMD ["target/release/planetwars"]

