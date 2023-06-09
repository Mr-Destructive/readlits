// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces
import type {Account, Client} from 'appwrite';

declare global {
	namespace App {
        interface Locals {
            client:  Client;
			account: Account<Preferences> | null;
        }
		// interface Error {}
		// interface Locals {}
		// interface PageData {}
		// interface Platform {}
	}
}
