'use babel';

import provider from './provider';

export default {
    getProvider() {
        // return a single provider, or an array of providers to use together
        return [provider];
    }
};
