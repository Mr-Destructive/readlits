<script lang="ts">
    import AddBook from '$lib/components/AddBook.svelte';
import Books from '../lib/components/Books.svelte';
import SignUp from '../lib/components/SignUp.svelte';
</script>
<div class="container h-full mx-auto flex justify-center items-center">
<div class="flex flex-col">
    <h2>Books</h2>
    <SignUp/>
    <Books />
    <AddBook/>
</div>
</div>
