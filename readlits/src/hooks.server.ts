import type { Handle } from "@sveltejs/kit";
import { Client } from "appwrite";

export const handle: Handle = async ({ event, resolve }) => {
    event.locals.client = new Client()
        .setEndpoint('http://127.0.0.1:8001/v1')
        .setProject('6467a226111048c72b2c');
    return resolve(event);
};
