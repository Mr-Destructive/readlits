<script>
  import { getContext, onMount } from 'svelte';
  
  const { book } = getContext('book');
  
  onMount(() => {
    
    const databases = new Databases(locals.client);
    const bookId = bok.$id;
    const book = await databases.getDocument('books', $bookId);
    console.log(book)
  });
</script>
