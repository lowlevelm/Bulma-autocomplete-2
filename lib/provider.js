'use babel';

// data source is an array of objects
import suggestions from '../data/autocomplete';

class IntermediateProvider {
	constructor() {
		// offer suggestions only when editing HTML files
		this.selector = '.text.html.basic, .text.html.vue, .text.html.jinja, .text.html.erb';
	}

	getSuggestions(options) {
		const { prefix } = options;

		// only look for suggestions after characters have been typed
		if (prefix.length >= 3) {
			return this.findMatchingSuggestions(prefix);
		}
	}

	findMatchingSuggestions(prefix) {
		// filter list of suggestions to those matching the prefix, case insensitive
		let prefixLower = prefix.toLowerCase();
		let matchingSuggestions = suggestions.filter((suggestion) => {
			let textLower = suggestion.text.toLowerCase();
			return textLower.startsWith(prefixLower);
		});

		// run each matching suggestion through inflateSuggestion() and return
		return matchingSuggestions.map(this.inflateSuggestion);
	}

	// clones a suggestion object to a new object with some shared additions
	// cloning also fixes an issue where selecting a suggestion won't insert it
	inflateSuggestion(suggestion) {
		return {
			text: suggestion.text,
			type: 'value',
			rightLabel: suggestion.sidetext ,
		};
	}
}
export default new IntermediateProvider();
