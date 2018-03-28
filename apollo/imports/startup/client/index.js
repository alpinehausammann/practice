import React from "react";
import { Meteor } from "meteor/meteor";
import { render } from "react-dom";
import { ApolloProvider } from "react-apollo";
import { ApolloClient } from "apollo-client";
import { HttpLink } from "apollo-cache-memory";
import { InMemoryCache } from "apollo-cache-inmemory";
import App from "../../ui/App";

const httpLink = new HttpLink({
    uri: MeteorUrl('graphql')
});

const cache = new InMemoryCache();

const client = new ApolloClient({
    link: httpLink,
    cache
});

const ApolloApp = () => (
    <ApolloProvider client={client}>
    <App />
    </ApolloProvider>
)

Meteor.startup(() => {
        render(<App />, document.getElementById('app'));
});
