<!-- <script>
	export let name;
</script>

<main>
	<h1>Hello {name}!</h1>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style> -->

<style>
  p {
    color: blue;
  }
</style>

<script>


  let rand = 0;
  function getRand() {
    fetch("./rand")
      .then(d => d.text())
      .then(d => (rand = d));
  }

  // Store the original title
const originalTitle = document.title;

// Listen for visibility changes
document.addEventListener("visibilitychange", function () {
  if (document.visibilityState === "hidden") {
    // User switched away from the tab
    document.title = "Come back! 😢";
  } else {
    // User returned to the tab
    document.title = originalTitle;
  }
});   

const theme = new URL(window.location).searchParams.get('theme');

			document.documentElement.classList.remove('light', 'dark');
			document.documentElement.classList.add(theme || 'light');

</script>

<h1>Your number is {rand}!</h1>
<button on:click={getRand}>Get a random number</button>
<p>Whatsap Sve;te</p>
% app.svelte %

<!-- <img src={img} alt="A descriptive alt text" /> -->