// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces
import type {Client} from 'appwrite';

declare global {
	namespace App {
        interface Locals {
            client:  Client;
        }
		// interface Error {}
		// interface Locals {}
		// interface PageData {}
		// interface Platform {}
	}
}
