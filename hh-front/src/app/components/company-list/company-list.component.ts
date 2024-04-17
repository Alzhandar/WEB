import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { Company } from '../../models/company.model';

@Component({
  selector: 'app-company-list',
  templateUrl: './company-list.component.html',
  styleUrls: ['./company-list.component.css']
})
export class CompanyListComponent implements OnInit {
  companies: Company[] = [];

  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.getCompanies();
  }

  getCompanies(): void {
    this.apiService.getCompanies().subscribe(
      (data: Company[]) => {
        this.companies = data;
      },
      error => {
        console.log('Error: ', error);
      }
    );
  }
}
