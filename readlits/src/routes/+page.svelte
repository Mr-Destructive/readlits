<script>
  import AddBook from '$lib/components/AddBook.svelte';
  import Books from '$lib/components/Books.svelte';
  import SignUp from '$lib/components/SignUp.svelte';
  import { Router, Route } from 'svelte-routing';
  import Home from '$lib/components/Home.svelte';
    import Login from '$lib/components/Login.svelte';
  
</script>



<nav class="flex items-center justify-between flex-wrap bg-teal-500 p-6">
  <div class="w-full block flex-grow lg:flex lg:items-center lg:w-auto">
    <div class="text-sm lg:flex-grow">
        <ul>
          <Router>
            <Login/>
            <AddBook/>
        </Router>
        </ul>
    </div>
  </div>
</nav>

<div class="container h-full mx-auto justify-center items-center">
<div class="flex flex-col">
    <h2>Books</h2>
    <Books />
</div>
</div>
