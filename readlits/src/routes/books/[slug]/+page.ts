import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';
import { Client, Databases } from 'appwrite';
export const load: PageLoad = async ({ params }) => {
  const title = params.slug;
  const client = new Client()
    .setEndpoint('http://127.0.0.1:8001/v1')
    .setProject('6467a226111048c72b2c');
  const databases = new Databases(client);
  try {
    const book = await databases.getDocument('6467a2917aaf8fd17198', '6467a33ecbefa946e984', title);
    const reviews = await databases.listDocuments(
    '6467a2917aaf8fd17198',
    '6472219e144e1f6135ea'
    );
    return {
      title: book.name,
      content: book.description,
      author: book.Author,
      rating: book.rating,
      cover_image: book.cover_image,
      genre: book.genre,
    };
  } catch (err) {
    console.log(err);
    return error(404, 'Book not found');
  }
};

