/*
 * Copyright 2017, GeoSolutions Sas.
 * All rights reserved.
 *
 * This source code is licensed under the BSD-style license found in the
 * LICENSE file in the root directory of this source tree.
 */
const React = require('react');
const {compose, mapPropsStream} = require('recompose');
const {isNil} = require('lodash');
const Message = require('../../../MapStore2/web/client/components/I18N/Message');
const Rx = require('rxjs');

const API = {
    "csw": require('../../../MapStore2/web/client/api/CSW'),
    "wms": require('../../../MapStore2/web/client/api/WMS'),
    "wmts": require('../../../MapStore2/web/client/api/WMTS'),
    "hev-e": require('../../api/HEVE')
};

const BorderLayout = require('../../../MapStore2/web/client/components/layout/BorderLayout');
const LoadingSpinner = require('../../../MapStore2/web/client/components/misc/LoadingSpinner');
const withVirtualScroll = require('../../../MapStore2/web/client/components/misc/enhancers/infiniteScroll/withInfiniteScroll');
const loadingState = require('../../../MapStore2/web/client/components/misc/enhancers/loadingState');
const emptyState = require('../../../MapStore2/web/client/components/misc/enhancers/emptyState');
const withControllableState = require('../../../MapStore2/web/client/components/misc/enhancers/withControllableState');
const CatalogForm = require('../../../MapStore2/web/client/components/catalog/CatalogForm');
// const {getCatalogRecords} = require('../../../MapStore2/web/client/utils/CatalogUtils');
const Icon = require('../../../MapStore2/web/client/components/misc/FitIcon');
const defaultPreview = <Icon glyph="geoserver" padding={20}/>;
const SideGrid = compose(
    loadingState(({loading, items = []} ) => items.length === 0 && loading),
    emptyState(
        ({loading, items = []} ) => items.length === 0 && !loading,
        {
            title: <Message msgId="catalog.noRecordsMatched" />,
            style: { transform: "translateY(50%)"}
        })

)(require('../../../MapStore2/web/client/components/misc/cardgrids/SideGrid'));
/*
 * converts record item into a item for SideGrid
 */
const resToProps = ({records, result = {}}) => ({
    items: (records || []).map((record = {}) => ({
        title: record.title,
        caption: record.identifier,
        description: record.description,
        preview: record.thumbnail ? <img src="thumbnail" /> : defaultPreview,
        icon: record.icon,
        record
    })),
    total: result && result.numberOfRecordsMatched
});
const PAGE_SIZE = 10;
/*
 * retrieves data from a catalog service and converts to props
 */
const loadPage = ({text, catalog = {}}, page = 0) => Rx.Observable
    .fromPromise(API[catalog.type].textSearch(catalog.url, page * PAGE_SIZE + (catalog.type === "csw" ? 1 : 0), PAGE_SIZE, text))
    .map((result) => ({result, records: result.records}))
    .map(resToProps);
const scrollSpyOptions = {querySelector: ".ms2-border-layout-body", pageSize: PAGE_SIZE};
/**
 * Compat catalog : Reusable catalog component, with infinite scroll.
 * You can simply pass the catalog to browse and the handler onRecordSelected.
 * @example
 * <CompactCatalog catalog={type: "csw", url: "..."} onSelected={selected => console.log(selected)} />
 * @name CompactCatalog
 * @memberof components.catalog
 * @prop {object} catalog the definition of the selected catalog as `{type: "wms"|"wmts"|"csw", url: "..."}`
 * @prop {object} selected the record selected. Passing this will show it as selected (highlighted) in the list. It will compare record's `identifier` property to guess the selected record in the list
 * @prop {function} onRecordSelected
 * @prop {boolean} showCatalogSelector if true shows the catalog selector - TODO
 * @prop {array} services TODO allow selection of catalog from a list
 * @prop {string} [searchText] the search text (if you want to control it)
 * @prop {function} [setSearchText] handler to get search text changes (if not defined, the component will control the text by it's own)
 */
module.exports = compose(
        withControllableState('searchText', "setSearchText", ""),
        withVirtualScroll({loadPage, scrollSpyOptions, hasMore: ({total, items}) => items.length < total}),
        mapPropsStream( props$ =>
            props$.merge(props$.take(1).switchMap(({catalog, loadFirst = () => {} }) =>
                props$
                    .debounceTime(500)
                    .startWith({searchText: "", catalog})
                    .distinctUntilKeyChanged('searchText')
                    .do(({searchText, catalog: nextCatalog} = {}) => loadFirst({text: searchText, catalog: nextCatalog}))
                    .ignoreElements() // don't want to emit props
        )))

)(({ setSearchText = () => { }, selected, onRecordSelected, loading, getCustomItem = () => ({}), searchText, items = [], total, catalog, services, showCatalogSelector, title, filterForm}) => {
    const Form = filterForm || CatalogForm;
    return (<BorderLayout
                className="compat-catalog"
        header={<Form services={services ? services : [catalog]} showCatalogSelector={showCatalogSelector} title={title} searchText={searchText} onSearchTextChange={setSearchText}/>}
                footer={<div className="catalog-footer">
                    <span>{loading ? <LoadingSpinner /> : null}</span>
                    {!isNil(total) ? <span className="res-info"><Message msgId="catalog.pageInfoInfinite" msgParams={{loaded: items.length, total}}/></span> : null}
                </div>}>
                <SideGrid
                    items={items.map(i =>
                        i === selected
                        || selected
                        && i && i.record
                        && selected.identifier === i.record.identifier
                            ? {...i, selected: true, ...getCustomItem(i)}
                            : {...i, ...getCustomItem(i)})}
                    loading={loading}
                    onItemClick={({record} = {}) => onRecordSelected(record, catalog)}/>
            </BorderLayout>);
});
