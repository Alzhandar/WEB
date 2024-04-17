// src/app/components/vacancy-list/vacancy-list.component.ts
import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { Vacancy } from '../../models/vacancy.model';

@Component({
  selector: 'app-vacancy-list',
  templateUrl: './vacancy-list.component.html',
  styleUrls: ['./vacancy-list.component.css']
})
export class VacancyListComponent implements OnInit {
    vacancies: Vacancy[] = [];

    constructor(private apiService: ApiService) {}

    ngOnInit(): void {
        this.apiService.getVacancies().subscribe(
            (data: Vacancy[]) => {
                this.vacancies = data;
            },
            error => {
                console.error('Error:', error);
            }
        );
    }
}
