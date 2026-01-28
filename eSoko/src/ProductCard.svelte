<script>
  import ProductImage from './ProductImage.svelte';

  const product = {
    name: 'Mac Mini',
    image: 'macminihero.png'
  };
</script>

<ProductImage imageName={product.image} />

<p>{product.name}</p>
