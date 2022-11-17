import { makeAutoObservable } from "mobx"
import { recordingsService } from "App/services"
import { IRecord } from 'App/services/RecordingsService'

export default class RecordingsStore {
  recordings: IRecord[] = []
  loading: boolean

  page = 1
  pageSize = 15
  order: 'desc' | 'asc' = 'desc'
  search = ''
  // not later we will add search by user id
  userId: number

  constructor() {
    makeAutoObservable(this)
  }

  updateSearch(val: string) {
    this.search = val
  }
  updatePage(page: number) {
    this.page = page
  }

  async fetchRecordings() {
    const filter = {
      page: this.page,
      limit: this.pageSize,
      order: this.order,
      search: this.search,
    }

    this.loading = true
    try {
      const recordings = await recordingsService.fetchRecordings(filter)
      this.recordings = recordings;
      this.fetchRecordingUrl(recordings[0].recordId)
      return recordings;
    } catch (e) {
      console.error(e)
    } finally {
      this.loading = false
    }
  }

  async fetchRecordingUrl(id: number): Promise<string> {
    this.loading = true
    try {
      const recording = await recordingsService.fetchRecording(id)
      return recording.URL;
    } catch (e) {
      console.error(e)
    } finally {
      this.loading = false
    }
  }

  async deleteRecording(id: number) {
    this.loading = true
    try {
      const recording = await recordingsService.deleteRecording(id)
      console.log(recording)
      return recording
    } catch (e) {
      console.error(e)
    } finally {
      this.loading = false
    }
  }


}