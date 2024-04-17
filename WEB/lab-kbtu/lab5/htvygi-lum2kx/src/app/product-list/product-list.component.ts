import { Component } from '@angular/core';
import { NgxGalleryOptions, NgxGalleryImage } from '@kolkov/ngx-gallery';
import { products, Product } from '../products';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent {
  products: Product[] = [...products];
  selectedImage: string | undefined;

  galleryOptions: NgxGalleryOptions[] = [
    {
      width: '600px',
      height: '400px',
      thumbnailsColumns: 4,
      imagePercent: 100,
      thumbnailsPercent: 20,
      thumbnailsMargin: 10,
      thumbnailMargin: 10,
    },
    // Add more options as needed
  ];

  share(productIndex: number) {
    const product = this.products[productIndex];
    window.location.href = product.website;
  }

  onNotify(){
    window.alert('You will be notified when the product goes on sale');
  }

  getGalleryImages(images?: string[]): NgxGalleryImage[] {
    return images ? images.map(image => ({ small: image, medium: image, big: image })) : [];
  }

  setMainImage(image: string, mainImageElement: HTMLImageElement) {
    mainImageElement.src = image;
    this.selectedImage = image; 
  }
}

/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/